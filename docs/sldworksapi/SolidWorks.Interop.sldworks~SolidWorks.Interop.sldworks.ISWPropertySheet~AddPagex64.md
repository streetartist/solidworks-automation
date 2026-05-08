# AddPagex64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddPagex64`

Adds a CPropertyPage-derived page to an ISWPropertySheet in 64-bit applications.
Adds a CPropertyPage-derived page to an [ISWPropertySheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.md) in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddPagex64( _
   ByVal Page As System.Long _
) As System.Integer
```

```

Dim instance As ISWPropertySheet
Dim Page As System.Long
Dim value As System.Integer
 
value = instance.AddPagex64(Page)
```

```

System.int AddPagex64( 
   System.long Page
)
```

```

System.int AddPagex64( 
   System.int64 Page
) 
```

#### Parameters

*Page*
:   Pointer to the CPropertyPage to add, cast to a long long

#### Return Value

True if successful, false if not

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISWPropertySheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.md)  
[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.md)  
[ISWPropertySheet::AddPage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddPage.md)
