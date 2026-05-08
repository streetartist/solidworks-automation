# Orientation Property (IPageSetup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~Orientation`

Gets or sets the page orientation.
Gets or sets the page orientation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Orientation As System.Integer
```

```

Dim instance As IPageSetup
Dim value As System.Integer
 
instance.Orientation = value
 
value = instance.Orientation
```

```

System.int Orientation {get; set;}
```

```

property System.int Orientation {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Page orientation as defined in [swPageSetupOrientation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPageSetupOrientation_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)
