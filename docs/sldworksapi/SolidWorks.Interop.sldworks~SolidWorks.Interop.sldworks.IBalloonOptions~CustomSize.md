# CustomSize Property (IBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~CustomSize`

Gets and sets the user-defined size of the balloon.
Gets and sets the user-defined size of the balloon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CustomSize As System.Double
```

```

Dim instance As IBalloonOptions
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

User-defined size of balloons; valid only when [IBalloonOptions::Size](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~Size.md) is set to [swBalloonFit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html).swBF\_UserDef

Remarks

See the SOLIDWORKS Help for additional details about balloons.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md)  
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.md)
