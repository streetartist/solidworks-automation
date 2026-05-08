# Origin Property (IPlaneManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Origin`

Gets or sets the origin of the plane.
Gets or sets the origin of the plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Origin As MathPoint
```

```

Dim instance As IPlaneManipulator
Dim value As MathPoint
 
instance.Origin = value
 
value = instance.Origin
```

```

MathPoint Origin {get; set;}
```

```

property MathPoint^ Origin {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

#### Property Value

[Origin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)

Remarks

If a plane with a manipulator is already displayed, then do not set a new [normal-to vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Normal.md) or origin for that plane.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.md)  
[IPlaneManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.md)
