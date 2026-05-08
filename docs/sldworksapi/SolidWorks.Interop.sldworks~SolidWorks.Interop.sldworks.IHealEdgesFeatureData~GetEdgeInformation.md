# GetEdgeInformation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~GetEdgeInformation`

Gets the number of edges before healing and the number of edges after healing.
Gets the number of edges before healing and the number of edges after healing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetEdgeInformation( _
   ByRef EdgeCountBefore As System.Integer, _
   ByRef EdgeCountAfter As System.Integer _
) 
```

```

Dim instance As IHealEdgesFeatureData
Dim EdgeCountBefore As System.Integer
Dim EdgeCountAfter As System.Integer
 
instance.GetEdgeInformation(EdgeCountBefore, EdgeCountAfter)
```

```

void GetEdgeInformation( 
   out System.int EdgeCountBefore,
   out System.int EdgeCountAfter
)
```

```

void GetEdgeInformation( 
   [Out] System.int EdgeCountBefore,
   [Out] System.int EdgeCountAfter
) 
```

#### Parameters

*EdgeCountBefore*
:   Number of edges before healing

*EdgeCountAfter*
:   Number of edges after healing

Example

[Modify Heal Edges Feature (VBA)](Modify_Heal_Edges_Feature_Example_VB.htm)  
[Get Heal Edges Feature Data (C#)](Get_Heal_Edges_Feature_Data_Example_CSharp.htm)  
[Get Heal Edges Feature Data (VB.NET)](Get_Heal_Edges_Feature_Data_Example_VBNET.htm)  
[Get Heal Edges Feature Data (VBA)](Get_Heal_Edges_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.md)  
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.md)
