# IsConverted Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsConverted`

Gets whether the active document was converted to the current release uponing opening but has not yet been saved.
Gets whether the active document was converted to the current release uponing opening but has not yet been saved.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsConverted() As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
value = instance.IsConverted()
```

```

System.bool IsConverted()
```

```

System.bool IsConverted(); 
```

#### Return Value

True if the active document was converted to the current release uponing opening but not yet been saved, false if not

Example

**Visual Basic for Applications (VBA)**

Option Explicit

Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swModelDocExt As SldWorks.ModelDocExtension  
Dim bool As Boolean

Sub Main()

Set swApp = CreateObject("Sldworks.Application")  
Set swModel = swApp.**ActiveDoc**  
Set swModelDocExt = swModel.**Extension**  
Debug.Print "Document converted to current release but not yet saved? " \_

> & swModelDocExt.**IsConverted**

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
