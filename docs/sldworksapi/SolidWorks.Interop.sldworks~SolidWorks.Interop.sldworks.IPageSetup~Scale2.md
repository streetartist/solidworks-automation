# Scale2 Property (IPageSetup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~Scale2`

Gets or sets the scale for printing the page.
Gets or sets the scale for printing the page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Scale2 As System.Double
```

```

Dim instance As IPageSetup
Dim value As System.Double
 
instance.Scale2 = value
 
value = instance.Scale2
```

```

System.double Scale2 {get; set;}
```

```

property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Print scale factor from 1% to 1000%

Remarks

This value is only used when [IPageSetup::ScaleToFit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~ScaleToFit.md) is set to false.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)
