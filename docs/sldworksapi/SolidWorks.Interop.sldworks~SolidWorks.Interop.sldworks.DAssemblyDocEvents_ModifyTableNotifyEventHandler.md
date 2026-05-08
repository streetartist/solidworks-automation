# DAssemblyDocEvents_ModifyTableNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ModifyTableNotifyEventHandler`

Notifies your program when a table has been modified in an assembly.
Notifies your program when a table has been modified in an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ModifyTableNotifyEventHandler( _
   ByVal TableAnnotation As TableAnnotation, _
   ByVal TableType As System.Integer, _
   ByVal reason As System.Integer, _
   ByVal RowInfo As System.Integer, _
   ByVal ColumnInfo As System.Integer, _
   ByVal DataInfo As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ModifyTableNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ModifyTableNotifyEventHandler( 
   TableAnnotation TableAnnotation,
   System.int TableType,
   System.int reason,
   System.int RowInfo,
   System.int ColumnInfo,
   System.string DataInfo
)
```

```

public delegate System.int DAssemblyDocEvents_ModifyTableNotifyEventHandler( 
   TableAnnotation^ TableAnnotation,
   System.int TableType,
   System.int reason,
   System.int RowInfo,
   System.int ColumnInfo,
   System.String^ DataInfo
)
```

#### Parameters

*TableAnnotation*
:   [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)

*TableType*
:   Type of table as defined in [swTableAnnotationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableAnnotationType_e.html)

*reason*
:   Reason as defined in [swModifyTableNotifyReason\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swModifyTableNotifyReason_e.html)

*RowInfo*
:   Index of modified row

*ColumnInfo*
:   Index of modified column

*DataInfo*
:   Modified string

Remarks

If developing a C++ application, use [swAssemblyModifyTableNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Fire Notification When Changing a Table in an Assembly Document (C#)](Fire_Notification_When_Changing_a_Table_in_an_Assembly_Document_Example_CSharp.htm)  
[Fire Notification When Changing a Table in an Assembly Document (VB.NET)](Fire_Notification_When_Changing_a_Table_in_an_Assembly_Document_Example_VBNET.htm)  
[Fire Notification When Changing a Table in an Assembly Document (VBA)](Fire_Notification_When_Changing_a_Table_in_an_Assembly_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ModifyTableNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ModifyTableNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
