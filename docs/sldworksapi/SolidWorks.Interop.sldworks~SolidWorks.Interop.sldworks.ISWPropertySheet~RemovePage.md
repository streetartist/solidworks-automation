# RemovePage Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~RemovePage`

Removes a CPropertyPage derived page from an ISWPropertySheet.
Removes a CPropertyPage derived page from an [ISWPropertySheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemovePage( _
   ByVal Page As System.Integer _
) As System.Integer
```

```

Dim instance As ISWPropertySheet
Dim Page As System.Integer
Dim value As System.Integer
 
value = instance.RemovePage(Page)
```

```

System.int RemovePage( 
   System.int Page
)
```

```

System.int RemovePage( 
   System.int Page
) 
```

#### Parameters

*Page*
:   CPropertyPage to add, cast to a long

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISWPropertySheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.md)  
[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.md)
