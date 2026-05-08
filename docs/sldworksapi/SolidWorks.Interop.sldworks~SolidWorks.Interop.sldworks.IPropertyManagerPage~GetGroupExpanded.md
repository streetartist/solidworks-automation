# GetGroupExpanded Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage~GetGroupExpanded`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGroupExpanded( _
   ByVal GroupID As System.Integer, _
   ByRef Status As System.Integer _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPage
Dim GroupID As System.Integer
Dim Status As System.Integer
Dim value As System.Boolean
 
value = instance.GetGroupExpanded(GroupID, Status)
```

```

System.bool GetGroupExpanded( 
   System.int GroupID,
   out System.int Status
)
```

```

System.bool GetGroupExpanded( 
   System.int GroupID,
   [Out] System.int Status
) 
```

#### Parameters

*GroupID*

*Status*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage.md)  
[IPropertyManagerPage Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage_members.md)
