# Select Method (ICenterMark)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~Select`

Selects the center mark.
Selects the center mark.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select( _
   ByVal Append As System.Boolean, _
   ByVal Data As System.Object _
) As System.Boolean
```

```

Dim instance As ICenterMark
Dim Append As System.Boolean
Dim Data As System.Object
Dim value As System.Boolean
 
value = instance.Select(Append, Data)
```

```

System.bool Select( 
   System.bool Append,
   System.object Data
)
```

```

System.bool Select( 
   System.bool Append,
   System.Object^ Data
) 
```

#### Parameters

*Append*
:   True appends the center mark to the selection list, false replaces the selection list with this center mark

*Data*
:   [SelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the center mark is selected, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.md)
