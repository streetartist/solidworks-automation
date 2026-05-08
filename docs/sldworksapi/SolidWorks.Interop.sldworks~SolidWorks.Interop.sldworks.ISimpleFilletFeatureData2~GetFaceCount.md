# GetFaceCount Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFaceCount`

Gets the number of faces on which to create a simple radius fillet.
Gets the number of faces on which to create a simple radius fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFaceCount( _
   ByVal WhichFaceList As System.Integer _
) As System.Integer
```

```

Dim instance As ISimpleFilletFeatureData2
Dim WhichFaceList As System.Integer
Dim value As System.Integer
 
value = instance.GetFaceCount(WhichFaceList)
```

```

System.int GetFaceCount( 
   System.int WhichFaceList
)
```

```

System.int GetFaceCount( 
   System.int WhichFaceList
) 
```

#### Parameters

*WhichFaceList*
:   Face as defined in [swSimpleFilletWhichFaces\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimpleFilletWhichFaces_e.html)

#### Return Value

Number of faces

Remarks

Call this method before calling [ISimpleFilletFeatureData2::IGetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFaces.md) to get the size of the array for that method.

Example

[Get Data for Simple Fillet (C#)](Get_Data_for_Simple_Fillet_Example_CSharp.htm)  
[Get Data for Simple Fillet (VB.NET)](Get_Data_for_Simple_Fillet_Example_VBNET.htm)  
[Get Data for Simple Fillet (VBA)](Get_Data_for_Simple_Fillet_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFaces.md)  
[ISimpleFilletFeatureData2::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetFaces.md)  
[ISimpleFilletFeatureData2::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetFaces.md)
