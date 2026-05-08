# DAssemblyDocEvents_InsertTableNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_InsertTableNotifyEventHandler`

Notifies your program when a table has been inserted in an assembly.
Notifies your program when a table has been inserted in an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_InsertTableNotifyEventHandler( _
   ByVal TableAnnotation As TableAnnotation, _
   ByVal TableType As System.String, _
   ByVal TemplatePath As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_InsertTableNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_InsertTableNotifyEventHandler( 
   TableAnnotation TableAnnotation,
   System.string TableType,
   System.string TemplatePath
)
```

```

public delegate System.int DAssemblyDocEvents_InsertTableNotifyEventHandler( 
   TableAnnotation^ TableAnnotation,
   System.String^ TableType,
   System.String^ TemplatePath
)
```

#### Parameters

*TableAnnotation*
:   [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)

*TableType*
:   Type of table as defined in [swTableAnnotationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableAnnotationType_e.html)

*TemplatePath*
:   Full path of template used to create this table

Remarks

If developing a C++ application, use [swAssemblyInsertTableNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Fire Notification When Inserting a Table in an Assembly Document (C#)](Fire_Notification_When_Inserting_a_Table_in_an_Assembly_Document_Example_CSharp.htm)  
[Fire Notification When Inserting a Table in an Assembly Document (VB.NET)](Fire_Notification_When_Inserting_a_Table_in_an_Assembly_Document_Example_VBNET.htm)  
[Fire Notification When Inserting a Table in an Assembly Document (VBA)](Fire_Notification_When_Inserting_a_Table_in_an_Assembly_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_InsertTableNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_InsertTableNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
