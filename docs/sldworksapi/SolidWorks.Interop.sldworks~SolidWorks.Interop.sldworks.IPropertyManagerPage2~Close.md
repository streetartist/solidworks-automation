# Close Method (IPropertyManagerPage2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close`

Closes the current page in the PropertyManager.
Closes the current page in the PropertyManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Close( _
   ByVal Okay As System.Boolean _
) 
```

```

Dim instance As IPropertyManagerPage2
Dim Okay As System.Boolean
 
instance.Close(Okay)
```

```

void Close( 
   System.bool Okay
)
```

```

void Close( 
   System.bool Okay
) 
```

#### Parameters

*Okay*
:   VARIANT\_True or VARIANT\_false

#### Return Value

|  |  |
| --- | --- |
| **When you call...** | **Then...** |
| Close(VARIANT\_True) | [IPropertyManagerPage2Handler8::OnClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnClose.md) is called with argument swPropertyManagerPageClose\_Okay, regardless of which buttons are displayed at the top of the page. |
| Close(VARIANT\_false) | [IPropertyManagerPage2Handler8::OnClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnClose.md) is called with argument swPropertyManagerPageClose\_Cancel, regardless of which buttons are displayed at the top of the page. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)  
[IPropertyManagerPage2::Show2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md)  
[IPropertyManagerPage2::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl.md)  
[IPropertyManagerPage2::AddGroupBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.md)  
[IPropertyManagerPage2::SetTitleBitmap2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap2.md)
