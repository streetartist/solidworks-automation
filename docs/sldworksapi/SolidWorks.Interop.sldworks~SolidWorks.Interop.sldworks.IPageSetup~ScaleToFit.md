# ScaleToFit Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~ScaleToFit`

Enables or disables scaling the page to fit the printer.
Enables or disables scaling the page to fit the printer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ScaleToFit As System.Boolean
```

```

Dim instance As IPageSetup
Dim value As System.Boolean
 
instance.ScaleToFit = value
 
value = instance.ScaleToFit
```

```

System.bool ScaleToFit {get; set;}
```

```

property System.bool ScaleToFit {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to scale page to fit the printer, false to not

Remarks

If this property is false, then you can use [IPageSetup::Scale2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~Scale2.md) to set the scaling factor.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)
