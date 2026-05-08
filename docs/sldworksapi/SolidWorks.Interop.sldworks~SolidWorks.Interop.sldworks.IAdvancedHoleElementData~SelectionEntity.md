# SelectionEntity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~SelectionEntity`

Gets or sets the entity used to specify the Up to Selection or Offset from Surface end condition for this Advanced Hole element.
Gets or sets the entity used to specify the Up to Selection or Offset from Surface end condition for this Advanced Hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectionEntity As System.Object
```

```

Dim instance As IAdvancedHoleElementData
Dim value As System.Object
 
instance.SelectionEntity = value
 
value = instance.SelectionEntity
```

```

System.object SelectionEntity {get; set;}
```

```

property System.Object^ SelectionEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

End condition entity

Remarks

This property is valid only when [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.md) is set to [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html):

- swEndCondOffsetFromSurface (end condition entity is a [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), or [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md))

    - or -

- swEndCondUpToSelection (end condition entity is a face, surface, or plane)

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md)  
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.md)
