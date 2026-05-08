# EntitiesToMate Property (IRackPinionMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~EntitiesToMate`

Gets or sets the entities to mate in this rack and pinion mate feature.
Gets or sets the entities to mate in this rack and pinion mate feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EntitiesToMate( _
   ByVal EntityType As System.Integer _
) As System.Object
```

```

Dim instance As IRackPinionMateFeatureData
Dim EntityType As System.Integer
Dim value As System.Object
 
instance.EntitiesToMate(EntityType) = value
 
value = instance.EntitiesToMate(EntityType)
```

```

System.object EntitiesToMate( 
   System.int EntityType
) {get; set;}
```

```

property System.Object^ EntitiesToMate {
   System.Object^ get(System.int EntityType);
   void set (System.int EntityType, System.Object^ value);
}
```

#### Parameters

*EntityType*
:   Entity type to mate as defined in [swRackPinionMateEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRackPinionMateEntityType_e.html)

#### Property Value

Array of entities to mate (see **Remarks**)

Remarks

If EntityType is set to swRackPinionMateEntityType\_e.:

- swRackPinionMateEntityType\_Pinion, then set the array with a a cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), circular [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) or [arc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md), sketch circle, [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md), or revolved [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md).
- swRackPinionMateEntityType\_Rack, then set the array with a linear edge, [sketch line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md), [centerline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.md), axis, or cylindrical face.

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities to mate using Mark = 64 for the rack and Mark = 128 for the pinion. You can pre-select mate entities during mate creation, but not during mate editing.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRackPinionMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.md)  
[IRackPinionMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData_members.md)
