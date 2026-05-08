# GetMouseDragMode Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMouseDragMode`

Gets whether the specified command-mouse mode is in effect.
Gets whether the specified command-mouse mode is in effect.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMouseDragMode( _
   ByVal Command As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Command As System.Integer
Dim value As System.Boolean
 
value = instance.GetMouseDragMode(Command)
```

```

System.bool GetMouseDragMode( 
   System.int Command
)
```

```

System.bool GetMouseDragMode( 
   System.int Command
) 
```

#### Parameters

*Command*
:   Command mode you wish to check as defined in [swMouseDragMode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseDragMode_e.html)

#### Return Value

True if the specified command is the currently running command, false if not

Remarks

This method determines if a special mouse mode is in use. Generally, these mouse modes are indicated visually with a different cursor and different mouse input interpretation. For example, one such mode is View Rotate mode. This is indicated visually to the user with a different cursor. When in this mode, the mouse input manipulates interactive view rotation, and the View Rotate toolbar button is pressed.

A complete list of valid mouse modes can be found in the [swMouseDragMode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseDragMode_e.html) enumeration.

The mouse mode applies to your whole SOLIDWORKS session, not a specific document. Therefore, if the user is currently working in an assembly document and is in Translate Assembly Component mode, then switching to a part or drawing document does not exit the mouse mode. If you call this method at this time to check for swTranslateAssemblyComponent, it returns True.

That mode is retained until a new command is entered, regardless if that this mode is not appropriate for a part or drawing document. When a new interactive command or API command runs, it terminates the Translate Assembly Component mode.

There is currently no general method to enable these mouse modes. However, several specific functions exist that enable or toggle certain modes. For example, [IAssemblyDoc::TranslateComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~TranslateComponent.md) and [IAssemblyDoc::RotateComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~RotateComponent.md). To disable any of these modes, use [IModelDoc2::SetPickMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetPickMode.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::SetMouseDragMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMouseDragMode.md)
