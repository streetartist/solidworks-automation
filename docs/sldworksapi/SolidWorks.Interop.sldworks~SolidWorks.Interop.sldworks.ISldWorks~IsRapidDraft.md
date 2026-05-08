# IsRapidDraft Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsRapidDraft`

Gets whether the specified drawing file is in SOLIDWORKS Detached format.
Gets whether the specified drawing file is in SOLIDWORKS Detached format.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsRapidDraft( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.IsRapidDraft(FileName)
```

```

System.bool IsRapidDraft( 
   System.string FileName
)
```

```

System.bool IsRapidDraft( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Name of the drawing file

#### Return Value

True if the file is in RapidDraft format, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
