# LockAngle Property (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~LockAngle`

Gets or sets whether the angle around the insertion point which to rotate this block instance is locked.
Gets or sets whether the angle around the insertion point which to rotate this block instance is locked.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LockAngle As System.Boolean
```

```

Dim instance As ISketchBlockInstance
Dim value As System.Boolean
 
instance.LockAngle = value
 
value = instance.LockAngle
```

```

System.bool LockAngle {get; set;}
```

```

property System.bool LockAngle {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to lock the angle of this block instance, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)  
[ISketchBlockInstance::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Angle.md)  
[ISketchBlockInstance::InstancePosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~InstancePosition.md)  
[ISketchBlockDefinition::InsertionPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~InsertionPoint.md)
