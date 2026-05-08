# DPartDocEvents_InsertTableNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_InsertTableNotifyEventHandler`

Notifies your program when a table has been inserted in a part.
Notifies your program when a table has been inserted in a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_InsertTableNotifyEventHandler( _
   ByVal TableAnnotation As TableAnnotation, _
   ByVal TableType As System.Integer, _
   ByVal TemplatePath As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_InsertTableNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_InsertTableNotifyEventHandler( 
   TableAnnotation TableAnnotation,
   System.int TableType,
   System.string TemplatePath
)
```

```

public delegate System.int DPartDocEvents_InsertTableNotifyEventHandler( 
   TableAnnotation^ TableAnnotation,
   System.int TableType,
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

If developing a C++ application, use [swPartInsertTableNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Example

[Fire Notification When Inserting a Table in a Part Document (C#)](Fire_Notification_When_Inserting_a_Table_in_a_Part_Document_Example_CSharp.htm)  
[Fire Notification When Inserting a Table in a Part Document (VB.NET)](Fire_Notification_When_Inserting_a_Table_in_a_Part_Document_Example_VBNET.htm)  
[Fire Notification When Inserting a Table in a Part Document (VBA)](Fire_Notification_When_Inserting_a_Table_in_a_Part_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_InsertTableNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_InsertTableNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
