# GetProcessID Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetProcessID`

Gets the process ID for the current SOLIDWORKS session.
Gets the process ID for the current SOLIDWORKS session.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetProcessID() As System.Integer
```

```

Dim instance As ISldWorks
Dim value As System.Integer
 
value = instance.GetProcessID()
```

```

System.int GetProcessID()
```

```

System.int GetProcessID(); 
```

#### Return Value

Process ID

Example

[Get Process ID of SOLIDWORKS Session (C#)](Get_Process_ID_of_SOLIDWORKS_Session_Example_CSharp.htm)  
[Get Process ID of SOLIDWORKS Session (VB.NET)](Get_Process_ID_of_SOLIDWORKS_Session_Example_VBNET.htm)  
[Get Process ID of SOLIDWORKS Session (VBA)](Get_Process_ID_of_SOLIDWORKS_Session_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
