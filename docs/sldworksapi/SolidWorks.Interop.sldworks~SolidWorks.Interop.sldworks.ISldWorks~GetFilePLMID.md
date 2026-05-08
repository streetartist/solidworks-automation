# GetFilePLMID Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFilePLMID`

Gets the Product Lifecycle Management (PLM) ID of the specified file stored in 3DEXPERIENCE.
Gets the Product Lifecycle Management (PLM) ID of the specified file stored in 3DEXPERIENCE.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFilePLMID( _
   ByVal FilePath As System.String _
) As System.String
```

```

Dim instance As ISldWorks
Dim FilePath As System.String
Dim value As System.String
 
value = instance.GetFilePLMID(FilePath)
```

```

System.string GetFilePLMID( 
   System.string FilePath
)
```

```

System.String^ GetFilePLMID( 
   System.String^ FilePath
) 
```

#### Parameters

*FilePath*
:   Name of file

#### Return Value

PLM ID

Remarks

This method is valid only for [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
