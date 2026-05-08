# SetApiUndoObject Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetApiUndoObject`

Implements an undo object for an add-in application.
Implements an undo object for an add-in application.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetApiUndoObject( _
   ByVal PHandler As System.Object, _
   ByVal DisplayName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim PHandler As System.Object
Dim DisplayName As System.String
Dim value As System.Boolean
 
value = instance.SetApiUndoObject(PHandler, DisplayName)
```

```

System.bool SetApiUndoObject( 
   System.object PHandler,
   System.string DisplayName
)
```

```

System.bool SetApiUndoObject( 
   System.Object^ PHandler,
   System.String^ DisplayName
) 
```

#### Parameters

*PHandler*
:   [Undo object](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwUndoAPIHandler.md)

*DisplayName*
:   Name to display in the SOLIDWORKS undo list

#### Return Value

True if the undo object is implemented, false if not

Example

[Automate Add-in's Undo Commands (VBA)](Automate_Add-in_s_Undo_Commands_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
