# EnableButton Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~EnableButton`

Sets whether to enable the buttons on the PropertyManager.
Sets whether to enable the buttons on the PropertyManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnableButton( _
   ByVal WhichOne As System.Integer, _
   ByVal Enable As System.Boolean _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPage2
Dim WhichOne As System.Integer
Dim Enable As System.Boolean
Dim value As System.Boolean
 
value = instance.EnableButton(WhichOne, Enable)
```

```

System.bool EnableButton( 
   System.int WhichOne,
   System.bool Enable
)
```

```

System.bool EnableButton( 
   System.int WhichOne,
   System.bool Enable
) 
```

#### Parameters

*WhichOne*
:   Button as defined in [swPropertyManagerPageButtons e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageButtons_e.html)

*Enable*
:   True enables the button, false disables it

#### Return Value

True if the button was enabled or disabled, false if not

Remarks

You can only call this method after the page is displayed.

By default, all of the specified buttons that appear at the top of the PropertyManager are initially enabled, except for the Previous Page button.

**NOTE:** The intended use of this method is to disable the Previous Page button when the first of multiple pages is displayed and to disable the Next Page button when the last of multiple pages is displayed. However, you can use it whenever you want.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)  
[IPropertyManagerPageButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageButton.md)
