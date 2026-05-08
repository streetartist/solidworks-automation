# GetIsFlipped Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetIsFlipped`

Gets whether the chamfer feature is flipped.
Gets whether the chamfer feature is flipped.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIsFlipped( _
   ByVal Entity As System.Object _
) As System.Boolean
```

```

Dim instance As IChamferFeatureData2
Dim Entity As System.Object
Dim value As System.Boolean
 
value = instance.GetIsFlipped(Entity)
```

```

System.bool GetIsFlipped( 
   System.object Entity
)
```

```

System.bool GetIsFlipped( 
   System.Object^ Entity
) 
```

#### Parameters

*Entity*
:   Edge, face, or loop

#### Return Value

True if the chamfer feature is flipped, false if not

Example

[Get Edge Chamfer Distances (C#)](Get_Edge_Chamfer_Distances_Example_CSharp.htm)  
[Get Edge Chamfer Distances (VB.NET)](Get_Edge_Chamfer_Distances_Example_VBNET.htm)  
[Get Edge Chamfer Distances (VBA)](Get_Edge_Chamfer_Distances_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.md)  
[IChamferFeatureData2::SetIsFlipped Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~SetIsFlipped.md)
