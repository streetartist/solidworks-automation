# LoadAddIn Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn`

Loads the specified add-in in SOLIDWORKS.
Loads the specified add-in in SOLIDWORKS.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadAddIn( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Integer
 
value = instance.LoadAddIn(FileName)
```

```

System.int LoadAddIn( 
   System.string FileName
)
```

```

System.int LoadAddIn( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Fully qualified file name of the add-in

#### Return Value

Status of loading the add-in as defined in [swLoadAddinError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLoadAddinError_e.html)

Remarks

You cannot load MBD using its add-in path. Instead, load the MBD add-in as follows:

> status = swApp.**LoadAddIn**('MBD')

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
[ISldWorks::UnloadAddIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnloadAddIn.md)
