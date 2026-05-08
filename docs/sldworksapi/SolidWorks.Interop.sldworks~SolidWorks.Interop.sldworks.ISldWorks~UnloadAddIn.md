# UnloadAddIn Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnloadAddIn`

Unloads the specified add-in from SOLIDWORKS.
Unloads the specified add-in from SOLIDWORKS.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UnloadAddIn( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Integer
 
value = instance.UnloadAddIn(FileName)
```

```

System.int UnloadAddIn( 
   System.string FileName
)
```

```

System.int UnloadAddIn( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Fully qualified file name of the add-in

#### Return Value

Status of unloading the add-in:

- 0: Successfully unloaded the add-in
- -1: Failed to unload the add-in due to some error condition

Remarks

You cannot unload MBD using its add-in path. Instead, unload the MBD add-in as follows:

> status = swApp.**UnloadAddIn**('MBD')

Example

[Load and Unload Add-in (C#)](Load_and_Unload_Add-in_Example_CSharp.htm)  
[Load and Unload Add-in (VB.NET)](Load_and_Unload_Add-in_Example_VBNET.htm)  
[Load and Unload Add-in (VBA)](Load_and_Unload_Add-in_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::LoadAddIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.md)
