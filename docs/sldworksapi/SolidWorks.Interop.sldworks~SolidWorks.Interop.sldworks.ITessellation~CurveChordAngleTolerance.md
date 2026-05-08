# CurveChordAngleTolerance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~CurveChordAngleTolerance`

Gets or sets the maximum angle, in radians, that is allowed between a chord and its originating curve.
Gets or sets the maximum angle, in radians, that is allowed between a chord and its originating curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurveChordAngleTolerance As System.Double
```

```

Dim instance As ITessellation
Dim value As System.Double
 
instance.CurveChordAngleTolerance = value
 
value = instance.CurveChordAngleTolerance
```

```

System.double CurveChordAngleTolerance {get; set;}
```

```

property System.double CurveChordAngleTolerance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Value for the curve chord angle tolerance

Remarks

This angle is calculated as the sum of the two angles between a chord and the curve tangents, measured at the chord ends.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)
