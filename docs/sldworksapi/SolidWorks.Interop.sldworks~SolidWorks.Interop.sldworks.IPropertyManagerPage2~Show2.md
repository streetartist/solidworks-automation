# Show2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2`

Shows the PropertyManager page.
Shows the PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Show2( _
   ByVal Options As System.Integer _
) As System.Integer
```

```

Dim instance As IPropertyManagerPage2
Dim Options As System.Integer
Dim value As System.Integer
 
value = instance.Show2(Options)
```

```

System.int Show2( 
   System.int Options
)
```

```

System.int Show2( 
   System.int Options
) 
```

#### Parameters

*Options*
:   Options as defined in [swPropertyManagerPageShowOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageShowOptions_e.html)

#### Return Value

Status as defined by [swPropertyManagerPageStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageStatus_e.html)

Remarks

If another PropertyManager page is already displayed and that page is receptive to being stacked upon, then setting swPropertyManagerPageShowOptions\_e to swPropertyManagerPageShowOptions\_StackPage will stack your PropertyManager page on it. When the user closes your PropertyManager page, the previous PropertyManager page is shown automatically.

**NOTE:** Typically SOLIDWORKS does not stack PropertyManager pages, and in the couple instances where SOLIDWORKS does, it is an agreement between the PropertyManager pages. The first PropertyManager page agrees that it can be stacked upon and allows the other known PropertyManager page to stack upon it. The mechanism is not a case of one PropertyManager page allowing any other generic PropertyManager page to be stacked upon it. It is assumed that the two pages are in agreement about what is going on and deal with it.

Using the API to stack ProertyManager pages is the same -- an add-in is the owner of both PropertyManager pages and knows what is going on and deals with it.  The concept of an API PropertyManager page wanting to know if it can stack upon the currently displayed PropertyManager page, whatever it might be, does not work because of the assumption that the first API PropertyManager page has knowledge of and allows another API PropertyManager page to stack on it.

If the PropertyManager page is locked, then stacking PropertyManager pages is not allowed. A PropertyManager page is locked if the Options argument of [ISldWorks::CreatePropertyManagerPage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreatePropertyManagerPage.md) or [ISldWorks::ICreatePropertyManagerPage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICreatePropertyManagerPage.md) was set to swPropertyManagerOptions\_LockedPage when the PropertyManager page was created.

Example

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)  
[IPropertyManagerPage2::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl.md)  
[IPropertyManagerPage2::AddGroupBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.md)  
[IPropertyManagerPage2::Close Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md)  
[IPropertyManagerPage2::SetTitleBitmap2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap2.md)
