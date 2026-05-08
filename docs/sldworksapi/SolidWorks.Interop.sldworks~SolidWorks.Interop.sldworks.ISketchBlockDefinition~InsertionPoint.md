# InsertionPoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~InsertionPoint`

Gets or sets the insertion point for the block definition.
Gets or sets the insertion point for the block definition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InsertionPoint As MathPoint
```

```

Dim instance As ISketchBlockDefinition
Dim value As MathPoint
 
instance.InsertionPoint = value
 
value = instance.InsertionPoint
```

```

MathPoint InsertionPoint {get; set;}
```

```

property MathPoint^ InsertionPoint {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

#### Property Value

[Insertion point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) for this block definition

Remarks

The insertion point of a block definition is the point around which instances of the block rotate or scale. It is the origin of the sketch containing the geometry that is part of the block definition. This implies that the base point of a block definition is always (0,0,0), because the sketch origin is (0,0). Therefore, get version of SketchBlockDefinition::InsertionPoint always returns (0,0,0).

The BlockDefinition::InsertionPoint values are specified relative to the current base point. However, when the insertion point is changed, it must become the sketch origin again, that is, it must become the (0,0,0) point again. So, if you use the this set/put version of this property and then immediately use get version of this property, it returns (0,0,0).

Changing the insertion point does not affect how instances of the block look in a drawing, so when the base point changes, the sketch geometry in the definition is adjusted to allow for that behavior. This means that if you get the block definition sketch and sketch geometry, the sketch geometry coordinates will be different after the insertion point is changed.

Example

[Get and Set Blocks in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockInstance::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Angle.md)  
[ISketchBlockInstance::InstancePosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~InstancePosition.md)  
[ISketchBlockInstance::LockAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~LockAngle.md)
