# ReferenceEntityType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntityType`

Gets the exact entity type returned by IMateReference::ReferenceEntity2.
Gets the exact entity type returned by [IMateReference::ReferenceEntity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntity2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ReferenceEntityType( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IMateReference
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.ReferenceEntityType(Index)
```

```

System.int ReferenceEntityType( 
   System.int Index
) {get;}
```

```

property System.int ReferenceEntityType {
   System.int get(System.int Index);
}
```

#### Parameters

*Index*
:   Mate reference entity as defined in [swMateReferenceIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceIndex_e.html)

#### Property Value

Value as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

Remarks

Call this property to determine the type returned by [IMateReference::ReferenceEntity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntity2.md). Then cast the object returned by IMateReference::ReferenceEntity2 into the appropriate type.

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
