# EnableFileMenu Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnableFileMenu`

Gets or sets whether to enable file-related menus and toolbars.
Gets or sets whether to enable file-related menus and toolbars.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableFileMenu As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
instance.EnableFileMenu = value
 
value = instance.EnableFileMenu
```

```

System.bool EnableFileMenu {get; set;}
```

```

property System.bool EnableFileMenu {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable file-related menus and toolbars (e.g., open a document, create a new document, open a recent document, etc.,); false to disable file-related menus and toolbars

Example

**Visual Basic for Applications (VBA)**

Option Explicit

Dim swApp As SldWorks.SldWorks  
Sub main()

Set swApp = Application.SldWorks

' Disable file-related menus and toolbars  
swApp.**EnableFileMenu** = False

' Enable file-related menus and toolbars

swApp.**EnableFileMenu** = True

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[IModelDoc2::Toolbars](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Toolbars.md)
