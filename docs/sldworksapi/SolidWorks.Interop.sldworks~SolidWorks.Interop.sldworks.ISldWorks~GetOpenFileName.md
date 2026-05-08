# GetOpenFileName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName`

Obsolete. Superseded by ISldWorks::GetOpenFileName2.
Obsolete. Superseded by [ISldWorks::GetOpenFileName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOpenFileName( _
   ByVal DialogTitle As System.String, _
   ByVal InitialFileName As System.String, _
   ByVal FileFilter As System.String, _
   ByRef OpenOptions As System.Integer, _
   ByRef ConfigName As System.String, _
   ByRef DisplayName As System.String _
) As System.String
```

```

Dim instance As ISldWorks
Dim DialogTitle As System.String
Dim InitialFileName As System.String
Dim FileFilter As System.String
Dim OpenOptions As System.Integer
Dim ConfigName As System.String
Dim DisplayName As System.String
Dim value As System.String
 
value = instance.GetOpenFileName(DialogTitle, InitialFileName, FileFilter, OpenOptions, ConfigName, DisplayName)
```

```

System.string GetOpenFileName( 
   System.string DialogTitle,
   System.string InitialFileName,
   System.string FileFilter,
   out System.int OpenOptions,
   out System.string ConfigName,
   out System.string DisplayName
)
```

```

System.String^ GetOpenFileName( 
   System.String^ DialogTitle,
   System.String^ InitialFileName,
   System.String^ FileFilter,
   [Out] System.int OpenOptions,
   [Out] System.String^ ConfigName,
   [Out] System.String^ DisplayName
) 
```

#### Parameters

*DialogTitle*
:   Title of the dialog

*InitialFileName*
:   Path and file name of the file to open

*FileFilter*
:   File name extension of the file to open

*OpenOptions*
:   Not used

*ConfigName*
:   Name of the configuration

*DisplayName*
:   Recommended file name to use

#### Return Value

Path and file name of the file to open

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.md)  
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.md)  
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.md)  
[ISldWorks::GetOpenedFileInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenedFileInfo.md)  
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.md)
