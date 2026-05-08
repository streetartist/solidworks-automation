# AddContextMenuFlyout Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~AddContextMenuFlyout`

Adds this flyout to the context menus of the specified documents and selections.
Adds this flyout to the context menus of the specified documents and selections.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddContextMenuFlyout( _
   ByVal DocumentType As System.Integer, _
   ByVal SelectionType As System.Integer _
) As System.Boolean
```

```

Dim instance As IFlyoutGroup
Dim DocumentType As System.Integer
Dim SelectionType As System.Integer
Dim value As System.Boolean
 
value = instance.AddContextMenuFlyout(DocumentType, SelectionType)
```

```

System.bool AddContextMenuFlyout( 
   System.int DocumentType,
   System.int SelectionType
)
```

```

System.bool AddContextMenuFlyout( 
   System.int DocumentType,
   System.int SelectionType
) 
```

#### Parameters

*DocumentType*
:   Type of document as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*SelectionType*
:   Type of object as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

True if successful, false if not

Remarks

Call this method once for each set of DocumentType and SelectionType parameters.

Context-sensitive menus support only the standard flyout style ([swCommandFlyoutStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandFlyoutStyle_e.html).swCommandFlyoutStyle\_Simple), in which there is no immediate action on the main flyout button.

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.md)  
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.md)
