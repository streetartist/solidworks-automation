# SetGroupRange Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage~SetGroupRange`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetGroupRange( _
   ByVal FirstGroupId As System.Integer, _
   ByVal FirstCheckId As System.Integer, _
   ByVal GroupCount As System.Integer _
) As System.Integer
```

```

Dim instance As IPropertyManagerPage
Dim FirstGroupId As System.Integer
Dim FirstCheckId As System.Integer
Dim GroupCount As System.Integer
Dim value As System.Integer
 
value = instance.SetGroupRange(FirstGroupId, FirstCheckId, GroupCount)
```

```

System.int SetGroupRange( 
   System.int FirstGroupId,
   System.int FirstCheckId,
   System.int GroupCount
)
```

```

System.int SetGroupRange( 
   System.int FirstGroupId,
   System.int FirstCheckId,
   System.int GroupCount
) 
```

#### Parameters

*FirstGroupId*

*FirstCheckId*

*GroupCount*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage.md)  
[IPropertyManagerPage Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage_members.md)
