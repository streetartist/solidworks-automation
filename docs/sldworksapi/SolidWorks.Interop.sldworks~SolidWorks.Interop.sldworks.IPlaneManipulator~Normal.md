# Normal Property (IPlaneManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Normal`

Gets or sets the normal-to vector for a plane that has a manipulator.
Gets or sets the normal-to vector for a plane that has a manipulator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Normal As MathVector
```

```

Dim instance As IPlaneManipulator
Dim value As MathVector
 
instance.Normal = value
 
value = instance.Normal
```

```

MathVector Normal {get; set;}
```

```

property MathVector^ Normal {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

#### Property Value

[Normal-to vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

Remarks

If a plane with a manipulator is already displayed, then do not set a new normal-to vector or [origin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Origin.md) for that plane.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.md)  
[IPlaneManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.md)
