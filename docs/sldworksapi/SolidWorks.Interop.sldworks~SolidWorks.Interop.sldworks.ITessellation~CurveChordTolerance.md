# CurveChordTolerance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~CurveChordTolerance`

Gets or sets the maximum permitted distance from a chord (facet fin) to the curve (edge entity).
Gets or sets the maximum permitted distance from a chord (facet fin) to the curve (edge entity).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurveChordTolerance As System.Double
```

```

Dim instance As ITessellation
Dim value As System.Double
 
instance.CurveChordTolerance = value
 
value = instance.CurveChordTolerance
```

```

System.double CurveChordTolerance {get; set;}
```

```

property System.double CurveChordTolerance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Value for the curve chord tolerance

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)
