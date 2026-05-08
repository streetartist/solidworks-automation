# ProjectionOption Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ProjectionOption`

Gets or sets whether the distance between the selected entities is projected.
Gets or sets whether the distance between the selected entities is projected.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProjectionOption As System.Integer
```

```

Dim instance As IMeasure
Dim value As System.Integer
 
instance.ProjectionOption = value
 
value = instance.ProjectionOption
```

```

System.int ProjectionOption {get; set;}
```

```

property System.int ProjectionOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Distance between the selected entities is projected as defined by [swMeasureProjectOnOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMeasureProjectOnOption_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.md)  
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.md)  
[IMeasure::SetProjectionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~SetProjectionEntity.md)  
[IMeasure::Projection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Projection.md)
