# IAddItems Method (IPropertyManagerPageListbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~IAddItems`

Adds items to the attached drop-down list for this list box.
Adds items to the attached drop-down list for this list box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IAddItems( _
   ByVal TextCount As System.Short, _
   ByRef Texts As System.String _
) 
```

```

Dim instance As IPropertyManagerPageListbox
Dim TextCount As System.Short
Dim Texts As System.String
 
instance.IAddItems(TextCount, Texts)
```

```

void IAddItems( 
   System.short TextCount,
   ref System.string Texts
)
```

```

void IAddItems( 
   System.short TextCount,
   System.String^% Texts
) 
```

#### Parameters

*TextCount*
:   Number of items to add to the listbox

*Texts*
:   - in-process, unmanaged C++: Pointer to an array of strings of items of size TextCount
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.md)  
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.md)  
[IPropertyManagerPageListbox::AddItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~AddItems.md)
