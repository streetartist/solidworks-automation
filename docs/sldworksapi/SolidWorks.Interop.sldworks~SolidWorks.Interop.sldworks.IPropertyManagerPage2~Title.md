# Title Property (IPropertyManagerPage2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Title`

Gets or sets the title of the PropertyManager page.
Gets or sets the title of the PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Title As System.String
```

```

Dim instance As IPropertyManagerPage2
Dim value As System.String
 
instance.Title = value
 
value = instance.Title
```

```

System.string Title {get; set;}
```

```

property System.String^ Title {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Title of PropertyManager page

Remarks

You can use this method whether the page is displayed or not.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)  
[IPropertyManagerPage2::SetTitleBitmap2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap2.md)
