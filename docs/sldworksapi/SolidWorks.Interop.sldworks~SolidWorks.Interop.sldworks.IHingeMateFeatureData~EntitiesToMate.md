# EntitiesToMate Property (IHingeMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~EntitiesToMate`

Gets or sets the entities to mate in this hinge mate.
Gets or sets the entities to mate in this hinge mate.

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

Dim instance As IHingeMateFeatureData
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
:   Type of entity as defined in [swHingeMateEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHingeMateEntityType_e.html)

#### Property Value

Array of mate entities (see **Remarks**)

Remarks

If EntityType is set to swHingeMateEntityType\_e.:

- swHingeMateEntityType\_Concentric, then select two mate entities as specified in the Remarks of [IConcentricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~EntitiesToMate.md).
- swHingeMateEntityType\_Coincident, then select two mate entities:
  1. [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) or planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)
  2. another plane or planar face, [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md), [reference point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md), or [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)
- swHingeMateEntityType\_Angle, then select two faces. This type is valid only if [IHingeMateFeatureData::AngleSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~AngleSelection.md) is set to true.

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities to mate using Mark = 1 for concentric entities, Mark = 32768 for coincident entities, and Mark = 65536 for angle faces. You can pre-select mate entities during mate creation, but not during mate editing.

Example

See the [IHingeMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHingeMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.md)  
[IHingeMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData_members.md)
