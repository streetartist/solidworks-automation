# GetMemberIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~GetMemberIndex`

Gets the index of the specified pulley member.
Gets the index of the specified pulley member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMemberIndex( _
   ByVal PulleyCompObject As System.Object _
) As System.Integer
```

```

Dim instance As IBeltChainFeatureData
Dim PulleyCompObject As System.Object
Dim value As System.Integer
 
value = instance.GetMemberIndex(PulleyCompObject)
```

```

System.int GetMemberIndex( 
   System.object PulleyCompObject
)
```

```

System.int GetMemberIndex( 
   System.Object^ PulleyCompObject
) 
```

#### Parameters

*PulleyCompObject*
:   Pulley component

#### Return Value

Zero-based index value

Remarks

To specify PulleyCompObject, use [IBeltChainFeatureData::PulleyComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyComponents.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)
