# EditDatumTargetSymbol Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~EditDatumTargetSymbol`

Obsolete. Superseded by IModelDoc2::EditDatumTargetSymbol.
Obsolete. Superseded by [IModelDoc2::EditDatumTargetSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditDatumTargetSymbol.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditDatumTargetSymbol( _
   ByVal Datum1 As System.String, _
   ByVal Datum2 As System.String, _
   ByVal Datum3 As System.String, _
   ByVal AreaStyle As System.Short, _
   ByVal AreaOutside As System.Boolean, _
   ByVal Value1 As System.Double, _
   ByVal Value2 As System.Double, _
   ByVal ValueStr1 As System.String, _
   ByVal ValueStr2 As System.String, _
   ByVal ArrowsSmart As System.Boolean, _
   ByVal ArrowStyle As System.Short, _
   ByVal LeaderLineStyle As System.Short, _
   ByVal LeaderBent As System.Boolean, _
   ByVal ShowArea As System.Boolean, _
   ByVal ShowSymbol As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim Datum1 As System.String
Dim Datum2 As System.String
Dim Datum3 As System.String
Dim AreaStyle As System.Short
Dim AreaOutside As System.Boolean
Dim Value1 As System.Double
Dim Value2 As System.Double
Dim ValueStr1 As System.String
Dim ValueStr2 As System.String
Dim ArrowsSmart As System.Boolean
Dim ArrowStyle As System.Short
Dim LeaderLineStyle As System.Short
Dim LeaderBent As System.Boolean
Dim ShowArea As System.Boolean
Dim ShowSymbol As System.Boolean
Dim value As System.Boolean
 
value = instance.EditDatumTargetSymbol(Datum1, Datum2, Datum3, AreaStyle, AreaOutside, Value1, Value2, ValueStr1, ValueStr2, ArrowsSmart, ArrowStyle, LeaderLineStyle, LeaderBent, ShowArea, ShowSymbol)
```

```

System.bool EditDatumTargetSymbol( 
   System.string Datum1,
   System.string Datum2,
   System.string Datum3,
   System.short AreaStyle,
   System.bool AreaOutside,
   System.double Value1,
   System.double Value2,
   System.string ValueStr1,
   System.string ValueStr2,
   System.bool ArrowsSmart,
   System.short ArrowStyle,
   System.short LeaderLineStyle,
   System.bool LeaderBent,
   System.bool ShowArea,
   System.bool ShowSymbol
)
```

```

System.bool EditDatumTargetSymbol( 
   System.String^ Datum1,
   System.String^ Datum2,
   System.String^ Datum3,
   System.short AreaStyle,
   System.bool AreaOutside,
   System.double Value1,
   System.double Value2,
   System.String^ ValueStr1,
   System.String^ ValueStr2,
   System.bool ArrowsSmart,
   System.short ArrowStyle,
   System.short LeaderLineStyle,
   System.bool LeaderBent,
   System.bool ShowArea,
   System.bool ShowSymbol
) 
```

#### Parameters

*Datum1*

*Datum2*

*Datum3*

*AreaStyle*

*AreaOutside*

*Value1*

*Value2*

*ValueStr1*

*ValueStr2*

*ArrowsSmart*

*ArrowStyle*

*LeaderLineStyle*

*LeaderBent*

*ShowArea*

*ShowSymbol*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
