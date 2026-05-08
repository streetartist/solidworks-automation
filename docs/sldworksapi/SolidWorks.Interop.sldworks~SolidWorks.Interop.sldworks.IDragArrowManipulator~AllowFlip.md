# AllowFlip Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~AllowFlip`

Gets or sets whether the unidirectional handle can change direction when dragged past length = 0.
Gets or sets whether the unidirectional handle can change direction when dragged past length = 0.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AllowFlip As System.Boolean
```

```

Dim instance As IDragArrowManipulator
Dim value As System.Boolean
 
instance.AllowFlip = value
 
value = instance.AllowFlip
```

```

System.bool AllowFlip {get; set;}
```

```

property System.bool AllowFlip {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to allow the unidirectional handle to change direction when dragged past length = 0, false to not (see **Remarks**)

Remarks

This property is valid only if [IDragArrowManipulator::ShowOppositeDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~ShowOppositeDirection.md) is false.

Example

See [IDragArrowManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md)  
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.md)
