# ThreadStartAngle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ThreadStartAngle`

Gets or sets the start angle of the thread of this thread feature
Gets or sets the start angle of the thread of this thread feature

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThreadStartAngle As System.Double
```

```

Dim instance As IThreadFeatureData
Dim value As System.Double
 
instance.ThreadStartAngle = value
 
value = instance.ThreadStartAngle
```

```

System.double ThreadStartAngle {get; set;}
```

```

property System.double ThreadStartAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 (default) < Thread start angle < 2\*pi radians

Remarks

Specify either a value or an equation that starts with an equal sign (=).

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
