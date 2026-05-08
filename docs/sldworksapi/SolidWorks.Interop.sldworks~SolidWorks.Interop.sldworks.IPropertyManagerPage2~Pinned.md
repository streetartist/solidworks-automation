# Pinned Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Pinned`

Gets or sets the state of the pushpin on a PropertyManager page.
Gets or sets the state of the pushpin on a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Pinned As System.Boolean
```

```

Dim instance As IPropertyManagerPage2
Dim value As System.Boolean
 
instance.Pinned = value
 
value = instance.Pinned
```

```

System.bool Pinned {get; set;}
```

```

property System.bool Pinned {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if pushpin is pressed, false if not

Remarks

|  |  |  |
| --- | --- | --- |
| **If the user clicks...** | **And PropertyManagerPage2::GetPinned is...** | **Then...** |
| x | True or false | [IPropertyManagerPage2Handler8::OnClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnClose.md)(swPropertyManagerPageClose\_Closed) is called, the dialog closes, and [IPropertyManagerPage2Handler8::AfterClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~AfterClose.md) is called. |
| check mark | True | [IPropertyManagerPage2Handler8::OnClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnClose.md)(swPropertyManagerPageClose\_Apply) is called, the dialog is not closed, [IPropertyManagerPage2Handler8::AfterClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~AfterClose.md) is not called. |
|  | false | [IPropertyManagerPage2Handler8::OnClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnClose.md)(swPropertyManagerPageClose\_Okay) is called, the dialog is closed, and [IPropertyManagerPage2Handler8::AfterClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~AfterClose.md) is called. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)
