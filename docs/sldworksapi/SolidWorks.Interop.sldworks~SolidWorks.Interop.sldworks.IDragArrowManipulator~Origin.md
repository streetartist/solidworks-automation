# Origin Property (IDragArrowManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Origin`

Gets or sets the origin of the handle.
Gets or sets the origin of the handle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Origin As MathPoint
```

```

Dim instance As IDragArrowManipulator
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

Pointer to [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) object

Remarks

Before calling this property to change the origin setting, set [IDragArrowManipulator::FixedLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~FixedLength.md) to true.

Example

See [IDragArrowManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md)  
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.md)
