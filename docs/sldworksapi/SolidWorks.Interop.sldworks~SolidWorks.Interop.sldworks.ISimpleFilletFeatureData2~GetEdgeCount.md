# GetEdgeCount Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetEdgeCount`

Gets the number of edges on which to create a simple radius fillet.
Gets the number of edges on which to create a simple radius fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEdgeCount() As System.Integer
```

```

Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer
 
value = instance.GetEdgeCount()
```

```

System.int GetEdgeCount()
```

```

System.int GetEdgeCount(); 
```

#### Return Value

Number of edges

Remarks

Call this method before calling [ISimpleFilletFeatureData2::IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetEdges.md) to get the size of the array for that method.

Example

[Get Simple Fillet Feature Data (VBA)](Get_Simple_Fillet_Feature_Data_Example_VB.htm)  
[Get Simple Fillet Feature Data (VB.NET)](Get_Simple_Fillet_Feature_Data_Example_VBNET.htm)  
[Get Simple Fillet Feature Data (C#)](Get_Simple_Fillet_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetEdges.md)  
[ISimpleFilletFeatureData2::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Edges.md)
