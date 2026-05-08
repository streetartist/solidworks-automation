# InsertModelAnnotations Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations`

Obsolete. Superseded by IDrawingDoc::InsertModelAnnotations3.
Obsolete. Superseded by [IDrawingDoc::InsertModelAnnotations3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertModelAnnotations( _
   ByVal Option As System.Integer, _
   ByVal AllTypes As System.Boolean, _
   ByVal Types As System.Integer, _
   ByVal AllViews As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim Option As System.Integer
Dim AllTypes As System.Boolean
Dim Types As System.Integer
Dim AllViews As System.Boolean
Dim value As System.Boolean
 
value = instance.InsertModelAnnotations(Option, AllTypes, Types, AllViews)
```

```

System.bool InsertModelAnnotations( 
   System.int Option,
   System.bool AllTypes,
   System.int Types,
   System.bool AllViews
)
```

```

System.bool InsertModelAnnotations( 
   System.int Option,
   System.bool AllTypes,
   System.int Types,
   System.bool AllViews
) 
```

#### Parameters

*Option*

*AllTypes*

*Types*

*AllViews*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
