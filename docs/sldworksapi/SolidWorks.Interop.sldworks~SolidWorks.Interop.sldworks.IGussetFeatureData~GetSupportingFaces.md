# GetSupportingFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~GetSupportingFaces`

Gets the two, adjacent, supporting faces for this gusset feature.
Gets the two, adjacent, supporting faces for this gusset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSupportingFaces( _
   ByRef PFace1 As Face2, _
   ByRef PFace2 As Face2 _
) As System.Boolean
```

```

Dim instance As IGussetFeatureData
Dim PFace1 As Face2
Dim PFace2 As Face2
Dim value As System.Boolean
 
value = instance.GetSupportingFaces(PFace1, PFace2)
```

```

System.bool GetSupportingFaces( 
   out Face2 PFace1,
   out Face2 PFace2
)
```

```

System.bool GetSupportingFaces( 
   [Out] Face2^ PFace1,
   [Out] Face2^ PFace2
) 
```

#### Parameters

*PFace1*
:   Pointer to the first [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) object

*PFace2*
:   Pointer to the second [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) object

#### Return Value

True if both faces are returned, false if not

Example

[Get Gusset Feature Data (C#)](Get_Gusset_Feature_Data_Example_CSharp.htm)  
[Get Gusset Feature Data (VB.NET)](Get_Gusset_Feature_Data_Example_VBNET.htm)  
[Get Gusset Feature Data (VBA)](Get_Gusset_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.md)  
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.md)  
[IGussetFeatureData::SetSupportingFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~SetSupportingFaces.md)
