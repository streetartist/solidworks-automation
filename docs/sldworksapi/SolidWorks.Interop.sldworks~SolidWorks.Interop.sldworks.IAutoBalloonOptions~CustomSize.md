# CustomSize Property (IAutoBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~CustomSize`

Gets and sets the user-defined size of the balloons.
Gets and sets the user-defined size of the balloons.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CustomSize As System.Double
```

```

Dim instance As IAutoBalloonOptions
Dim value As System.Double
 
instance.CustomSize = value
 
value = instance.CustomSize
```

```

System.double CustomSize {get; set;}
```

```

property System.double CustomSize {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

User-defined size of the balloons; valid only when [IAutoBalloonOptions::Size](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~Size.md) is set to [swBalloonFit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html).swBF\_UserDef

Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)  
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.md)
