# EntitiesToMate Property (IGearMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData~EntitiesToMate`

Gets or sets the entities to mate in this gear mate.
Gets or sets the entities to mate in this gear mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EntitiesToMate As System.Object
```

```

Dim instance As IGearMateFeatureData
Dim value As System.Object
 
instance.EntitiesToMate = value
 
value = instance.EntitiesToMate
```

```

System.object EntitiesToMate {get; set;}
```

```

property System.Object^ EntitiesToMate {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of two entities to mate (cylindrical or conical [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [axes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md), or linear [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md))

Remarks

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

Example

See the [IGearMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGearMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.md)  
[IGearMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData_members.md)
