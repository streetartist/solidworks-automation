# ReferenceEntityCount Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntityCount`

Gets the number of mate reference entities for the selected mate reference.
Gets the number of mate reference entities for the selected mate reference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ReferenceEntityCount As System.Integer
```

```

Dim instance As IMateReference
Dim value As System.Integer
 
value = instance.ReferenceEntityCount
```

```

System.int ReferenceEntityCount {get;}
```

```

property System.int ReferenceEntityCount {
   System.int get();
}
```

#### Property Value

Number of mate reference entities

Remarks

This method returns a value 3 (primary, secondary, and tertiary).

Call this property before calling [IMateReference::ReferenceAlignment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceAlignment.md), [IMateReference::ReferenceEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntity.md), or [IMateReference::ReferenceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceType.md).

Example

[Get Mate Reference Properties (VBA)](Get_Mate_Reference_Properties_Example_VB.htm)  
[Get Mate Reference Properties (VB.NET)](Get_Mate_Reference_Properties_Example_VBNET.htm)  
[Get Mate Reference Properties (C#)](Get_Mate_Reference_Properties_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.md)  
[IMateReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.md)
